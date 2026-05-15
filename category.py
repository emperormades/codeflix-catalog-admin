from uuid import uuid4

class Category:
    def __init__(
        self,
        name,
        id = "",
        description = "",
        is_active = True,
    ) -> None:
        self.id = id or uuid4()
        self.name = name
        self.description = description
        self.is_active = is_active

        if len(self.name) > 255:
            raise ValueError("Name must be less than 256 characters")

    def __str__(self) -> str:
        return f"Category(id={self.id}, name={self.name}, description={self.description}, is_active={self.is_active})"

    def __repr__(self) -> str:
        return f"Category(id={self.id}, name={self.name}, description={self.description}, is_active={self.is_active})"