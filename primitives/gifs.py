import os
import tqdm
import numpy as np
import jax
from PIL import Image
from craftax.craftax.constants import Action

from .wrapper import SaveStateWrapper


def process_environment_step(
    env: SaveStateWrapper, renderer, state, action, rng, env_params, img_array
):
    """Processes an environment step and adds the rendered image to img_array."""
    obs, state, reward, done, info = env.step(action)

    image_array = renderer.render_craftax_pixels(
        state, 16
    )  # Assuming '16' is pixel size
    img = Image.fromarray(np.array(image_array, dtype=np.uint8))
    img_array.append(img)
    return obs, state, reward, done, info


def create_gif_grid(
    gif_arrays, save_path, grid_size, file_name="grid_output.gif"
):
    """Creates a grid of GIFs and saves it as a single large GIF."""
    num_gifs = len(gif_arrays)
    rows, cols = grid_size
    gif_length = max(
        len(gif) for gif in gif_arrays
    )  # Ensure all GIFs are the same length

    # Get width and height from the first image in the first GIF
    width, height = gif_arrays[0][0].size

    # Create a blank grid image for each frame in the GIF
    grid_frames = []
    black_frame = Image.new("RGB", (width, height), (0, 0, 0))

    for frame_idx in range(gif_length):
        grid_image = Image.new("RGB", (cols * width, rows * height))

        for gif_idx, gif in enumerate(gif_arrays):
            row = gif_idx // cols
            col = gif_idx % cols
            if frame_idx < len(gif):
                gif_frame = gif[frame_idx]
            else:
                gif_frame = black_frame  # gif[-1]  # If a GIF is shorter, make the black screen

            # Paste the GIF frame into the grid
            grid_image.paste(gif_frame, (col * width, row * height))

        grid_frames.append(grid_image)

    # Save the grid as a GIF
    gif_save_path = f"{save_path}"
    os.makedirs(gif_save_path, exist_ok=True)

    grid_frames[0].save(
        os.path.join(gif_save_path, file_name),
        save_all=True,
        append_images=grid_frames[1:],
        loop=0,
        duration=200,
    )


def visual_testing(
    random_seed: int,
    file_path: str,
    path_to_save: str,
    num_tries,
    env,
    renderer,
    grid_size=(2, 2),
):
    """Tests a function in the environment and generates a GIF grid from the steps."""
    rngs = jax.random.split(jax.random.PRNGKey(random_seed), num_tries)
    all_gif_arrays = []

    for rng in tqdm.tqdm(rngs):
        img_array = []
        try:
            obs, state = env.reset(rng, env.default_params)
            _, subrng = jax.random.split(rng)
            done = False

            # actions = function_to_test(state, **function_parameters)
            if not os.path.exists(file_path):
                raise ValueError(f"No such file in given path: {file_path}")

            with open(file_path, "r") as f:
                actions = []
                for line in f:
                    actions.append(Action(int(line.strip())))

            # assert len(actions) != 0, 'No actions found for this test function'

            i = 0
            while not done:
                # action = function_to_test(obs, **function_parameters)
                obs, state, reward, done, info = process_environment_step(
                    env,
                    renderer,
                    state,
                    actions[i],
                    subrng,
                    env.default_params,
                    img_array,
                )

                i += 1
                if i >= len(actions):
                    done = True

        except Exception as e:
            print(f"Error during testing: {e}")
            continue

        # Store each gif array to be used for grid creation later
        all_gif_arrays.append(img_array)

    # Generate the grid of GIFs
    # print(path_to_save)
    create_gif_grid(all_gif_arrays, path_to_save, grid_size)
