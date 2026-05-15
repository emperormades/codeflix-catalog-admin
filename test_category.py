import pytest, re, unittest
from faker import Faker

from uuid import UUID, uuid4
from category import Category

class TestCategory(unittest.TestCase):
    faker = Faker()
    word = faker.word()
    id = uuid4()

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
            Category(name=self.word * 256)


    def test_category_must_be_created_with_id_as_uuid(self):
        category = Category(name=self.faker.word())
        assert isinstance(category.id, UUID)

    def test_category_must_be_created_with_default_values(self):
        category = Category(name=self.word)
        assert category.name == self.word
        assert category.description == ""
        assert category.is_active == True

    def test_category_is_created_with_provided_values(self):
        category = Category(name=self.word)
        assert category.name == self.word
        assert category.is_active == True

    def test_Category_str_representation(self):
        category = Category(id=self.id, name=self.word)
        assert str(category) == f"Category(id={self.id}, name={self.word}, description=, is_active=True)"


    def test_Category_repr_representation(self):
        category = Category(id=self.id, name=self.word)
        assert repr(category) == f"Category(id={self.id}, name={self.word}, description=, is_active=True)"