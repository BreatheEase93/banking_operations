import pytest
from srs.processing import filter_by_state, sort_by_date
from tests.conftest import empty_list, empty_number, empty_string, by_state


@pytest.mark.parametrize('state, expected',[
    ("EXECUTED",
[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
 {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]),
    ("CANCELED",
 [{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
 {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]),
])

def test_filter_by_state(by_state, state, expected):
    assert filter_by_state(by_state, state) ==  expected


def test_filter_by_state_all(empty_list, empty_number, empty_string,by_state):
    assert filter_by_state(empty_list) == "Неверный список"
    assert filter_by_state(empty_number) == "Неверный список"
    assert filter_by_state(empty_string) == "Неверный список"
    assert filter_by_state(by_state,"121") == "Неправельный параметр state"