from .exc3 import Sorter
import pytest

class Test_Sorter:

    @pytest.fixture
    def names(self):
        return ['Anna','Marzena','Amadeusz','Kamil']

    def test_create_sorter(self):
        sorter = Sorter()
        assert isinstance(sorter, Sorter)


    def test_alhpabetical_first(self, names):
        #given
        sort = Sorter()

        #when
        sorted_names = sort.sorter(names, first_letter = True)

        #then
        assert sorted_names == ['Amadeusz','Anna','Kamil','Marzena']

    def test_alhpabetical_last(self, names):
        #given
        sort = Sorter()

        #when
        sorted_names = sort.sorter(names, last_letter = True)

        #then
        assert sorted_names == ['Marzena','Anna','Kamil','Amadeusz']

    def test_length(self, names):
        #given
        sort = Sorter()

        #when
        sorted_names = sort.sorter(names, length = True)


        #then
        assert sorted_names == ['Anna','Kamil','Marzena','Amadeusz']


