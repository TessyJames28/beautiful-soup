def filter(unfamiliar_skills, skills):
    for unfamiliar_skill in unfamiliar_skills:
        if unfamiliar_skill in skills:
            return False
    return True