import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from model_bakery import baker

from students.models import Course, Student


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def student():
    return Student.objects.create(name='Alex')


@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)

    return factory


@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)

    return factory


@pytest.mark.django_db
def test_get_first_course(api_client, course_factory):
    course_factory(_quantity=3)
    url = reverse('courses-detail', kwargs={'pk': 1})
    response = api_client.get(url)
    assert response.status_code == 200
    data = response.json()
    assert data['id'] == 1


@pytest.mark.django_db
def test_get_list_course(api_client, course_factory):
    course_factory(_quantity=3)
    url = reverse('courses-list')
    response = api_client.get(url)
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 3


@pytest.mark.django_db
def test_course_filter_id(api_client, course_factory):
    course = course_factory(id=10, name='alex')
    url = reverse('courses-list')
    response = api_client.get(url+f'?id={course.id}')
    data = response.json()
    assert response.status_code == 200
    assert data[0]['id'] == course.id


@pytest.mark.django_db
def test_course_filter_name(api_client, course_factory):
    course = course_factory(id=10, name='alex')
    url = reverse('courses-list')
    response = api_client.get(url + f'?name={course.name}')
    data = response.json()
    assert response.status_code == 200
    assert data[0]['name'] == course.name


@pytest.mark.django_db
def test_create_course(api_client, student):
    count = Course.objects.count()
    url = reverse('courses-list')
    course_data = {'name': 'Django',
                   'student': student.id
                   }
    response = api_client.post(url, data=course_data)
    assert response.status_code == 201
    assert Course.objects.count() == count + 1
    assert api_client.get(url, course_data)


@pytest.mark.django_db
def test_update_course(api_client, course_factory):
    course = course_factory()
    old_course_name = course.name
    url = reverse('courses-detail', kwargs={'pk': course.id})
    course_data = {'name': 'Django',
                   }
    response = api_client.patch(url, data=course_data)
    data = response.json()
    assert response.status_code == 200
    assert data['name'] == 'Django'
    assert old_course_name != data['name']


@pytest.mark.django_db
def test_delete_course(api_client, course_factory):
    course = course_factory()
    url = reverse('courses-detail', kwargs={'pk': course.id})
    response = api_client.delete(url)
    assert response.status_code == 204
    response = api_client.get(url)
    assert response.status_code == 404
