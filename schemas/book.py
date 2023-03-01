from _collections_abc import Mapping
from collections.abc import MutableMapping
from _collections_abc import Sequence
from ma import ma
from models.book import BookModel

class BookSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = BookModel
        load_instance = True