from PIL import Image
import numpy as np
from IPython.display import display
import craftax.craftax.renderer as renderer
__imgs = []
def display_state(state):
    image_array = renderer.render_craftax_pixels(state, block_pixel_size = 64)
    img = Image.fromarray(np.array(image_array, dtype=np.uint8))
    __imgs.append(img)
def save_gif(output_path = "logs/visualisation.gif", duration = 0.5, loop = 0):
    __imgs[0].save(
        output_path,
        save_all=True,
        append_images=__imgs[1:],
        duration=duration,
        loop=loop
    )