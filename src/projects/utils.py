def path_to_save_project_photo(instance: object, filename: str) -> str:
    """
    Возвращает путь сохранения фото для проектов.
    """

    return f"projects/{instance.project.number}/{filename}"
