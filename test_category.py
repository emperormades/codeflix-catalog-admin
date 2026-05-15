import pytest, re, unittest
from uuid import UUID, uuid4
from category import Category

class TestCategory(unittest.TestCase):
    def test_name_is_required(self):
        with pytest.raises(
            TypeError,
            match=re.escape("Category.__init__() missing 1 required positional argument: 'name'")
        ):
            Category()

    def test_name_must_have_less_than_256_characters(self):
        with pytest.raises(
            ValueError,
            match="Name must be less than 256 characters"
        ):
            Category(name="a" * 256)


    def test_category_must_be_created_with_id_as_uuid(self):
        category = Category(name="test")
        assert isinstance(category.id, UUID)

    def test_category_must_be_created_with_default_values(self):
        category = Category(name="test")
        assert category.name == "test"
        assert category.description == ""
        assert category.is_active == True

    def test_category_is_created_with_provided_values(self):
        category = Category(name="Filme")
        assert category.name == "Filme"
        assert category.is_active == True

    def test_Category_str_representation(self):
        id = uuid4()
        category = Category(id=id, name="Filme")
        assert str(category) == f"Category(id={id}, name=Filme, description=, is_active=True)"


    def test_Category_repr_representation(self):
        id = uuid4()
        category = Category(id=id, name="Filme")
        assert repr(category) == f"Category(id={id}, name=Filme, description=, is_active=True)"