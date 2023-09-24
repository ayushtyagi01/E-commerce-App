def paginate(items, skip: int, limit: int):
    return items[skip : skip + limit]
