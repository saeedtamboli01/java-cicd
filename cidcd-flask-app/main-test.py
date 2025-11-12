"""Pytest suite for validating the Flask app homepage."""

import pytest
from datetime import datetime
from app import app

@pytest.fixture
def client():
    """Create a test client for the Flask app."""
    app.config['TESTING'] = True
    with app.test_client() as test_client:
        yield test_client

def test_home_status_code(client):
    """Ensure the home route returns HTTP 200."""
    response = client.get('/')
    assert response.status_code == 200

def test_home_template_data(client):
    """Verify homepage content includes expected features, metrics, and current year."""
    response = client.get('/')
    html = response.data.decode()

    # Feature titles
    assert "Personalized Learning" in html
    assert "World-class Mentors" in html
    assert "Hands-on Projects" in html

    # Metrics
    assert "1M+" in html
    assert "2K+" in html
    assert "150+" in html

    # Current year
    current_year = str(datetime.now().year)
    assert current_year in html