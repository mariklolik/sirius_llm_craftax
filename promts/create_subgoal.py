def subgoal_prompt_templatenc(state, final_task):
    inventory = state.inventory

    text = open("curriculum_task_decomposition.txt", "r").read()
    text = text.format(inventory, final_task)
    return text
