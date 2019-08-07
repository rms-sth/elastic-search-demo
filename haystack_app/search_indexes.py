import datetime
from haystack import indexes
from haystack_app.models import Note, Customer


class NoteIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    author = indexes.CharField(model_attr='user')
    pub_date = indexes.DateTimeField(model_attr='pub_date')

    def get_model(self):
        return Note

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(pub_date__lte=datetime.datetime.now())


class CustomerIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.EdgeNgramField(document=True, use_template=True)
    first_name = indexes.CharField(model_attr='first_name')
    last_name = indexes.CharField(model_attr='last_name')
    other_names = indexes.CharField(model_attr='other_names')
    email = indexes.CharField(model_attr='email', default=" ")
    phone = indexes.CharField(model_attr='phone', default=" ")
    balance = indexes.IntegerField(model_attr='balance', default="0")
    customer_status = indexes.CharField(model_attr='customer_status')
    address = indexes.CharField(model_attr='address', default=" ")

    def get_model(self):
        return Customer

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
