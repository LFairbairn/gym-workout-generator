"""
Frontend tests using Playwright.

These tests open a real browser and interact with the web page
just like a user would - clicking buttons, filling forms, etc.
"""

import pytest
from playwright.sync_api import Page, expect


# The base URL where our app is running (Docker serves it on port 80)
BASE_URL = "http://localhost"


class TestHomePage:
    """Tests for the home page loading correctly."""

    def test_page_title(self, page: Page):
        """Check that the page title is correct."""
        # Go to the home page
        page.goto(BASE_URL)

        # Check the browser tab title
        expect(page).to_have_title("Gym Workout Generator")

    def test_header_visible(self, page: Page):
        """Check that the main header is visible."""
        page.goto(BASE_URL)

        # Find the h1 element and check its text
        header = page.locator("h1")
        expect(header).to_have_text("Gym Workout Generator")

    def test_form_elements_present(self, page: Page):
        """Check that all form elements are on the page."""
        page.goto(BASE_URL)

        # Check dropdown menus exist
        expect(page.locator("#workout-type")).to_be_visible()
        expect(page.locator("#difficulty")).to_be_visible()

        # Check duration slider exists
        expect(page.locator("#duration")).to_be_visible()

        # Check generate button exists
        expect(page.locator("#generate-btn")).to_be_visible()


class TestWorkoutGeneration:
    """Tests for generating workouts."""

    def test_generate_strength_workout(self, page: Page):
        """Test generating a strength workout."""
        page.goto(BASE_URL)

        # Fill in the form
        page.select_option("#workout-type", "strength")
        page.select_option("#difficulty", "beginner")

        # Click the generate button
        page.click("#generate-btn")

        # Wait for results to appear (they start hidden)
        results = page.locator("#results")
        expect(results).to_be_visible()

        # Check that exercises are displayed
        exercise_cards = page.locator(".exercise-card")
        expect(exercise_cards.first).to_be_visible()

    def test_generate_cardio_workout(self, page: Page):
        """Test generating a cardio workout."""
        page.goto(BASE_URL)

        # Fill in the form
        page.select_option("#workout-type", "cardio")
        page.select_option("#difficulty", "beginner")

        # Click generate
        page.click("#generate-btn")

        # Wait for results
        results = page.locator("#results")
        expect(results).to_be_visible()

        # Should show exercises
        exercise_cards = page.locator(".exercise-card")
        expect(exercise_cards.first).to_be_visible()

    def test_generate_flexibility_workout(self, page: Page):
        """Test generating a flexibility workout."""
        page.goto(BASE_URL)

        page.select_option("#workout-type", "flexibility")
        page.select_option("#difficulty", "beginner")
        page.click("#generate-btn")

        results = page.locator("#results")
        expect(results).to_be_visible()

    def test_workout_summary_shows_details(self, page: Page):
        """Test that workout summary displays key information."""
        page.goto(BASE_URL)

        page.select_option("#workout-type", "strength")
        page.select_option("#difficulty", "intermediate")
        page.click("#generate-btn")

        # Check summary section has content
        summary = page.locator("#workout-summary")
        expect(summary).to_contain_text("Workout Type")
        expect(summary).to_contain_text("Difficulty")
        expect(summary).to_contain_text("Duration")


class TestDurationSlider:
    """Tests for the duration slider functionality."""

    def test_slider_updates_display(self, page: Page):
        """Test that moving the slider updates the displayed value."""
        page.goto(BASE_URL)

        # Get the duration display element
        duration_display = page.locator("#duration-value")

        # Default should be 30
        expect(duration_display).to_have_text("30")

        # Change the slider value using JavaScript
        # (Playwright can't easily drag sliders, so we set value directly)
        page.evaluate("document.getElementById('duration').value = 60")
        page.evaluate("document.getElementById('duration').dispatchEvent(new Event('input'))")

        # Check the display updated
        expect(duration_display).to_have_text("60")


class TestMuscleGroupSelection:
    """Tests for muscle group checkbox selection."""

    def test_can_select_muscle_groups(self, page: Page):
        """Test that muscle group checkboxes can be selected."""
        page.goto(BASE_URL)

        # Find and click the chest checkbox
        chest_checkbox = page.locator("input[value='chest']")
        chest_checkbox.check()

        # Verify it's checked
        expect(chest_checkbox).to_be_checked()

    def test_multiple_muscle_groups(self, page: Page):
        """Test selecting multiple muscle groups."""
        page.goto(BASE_URL)

        # Select multiple muscle groups
        page.locator("input[value='chest']").check()
        page.locator("input[value='back']").check()
        page.locator("input[value='legs']").check()

        # Verify all are checked
        expect(page.locator("input[value='chest']")).to_be_checked()
        expect(page.locator("input[value='back']")).to_be_checked()
        expect(page.locator("input[value='legs']")).to_be_checked()


class TestNewWorkoutButton:
    """Tests for the 'Generate Another Workout' button."""

    def test_new_workout_hides_results(self, page: Page):
        """Test that clicking 'Generate Another' hides results and shows form."""
        page.goto(BASE_URL)

        # Generate a workout first
        page.select_option("#workout-type", "strength")
        page.select_option("#difficulty", "beginner")
        page.click("#generate-btn")

        # Wait for results
        results = page.locator("#results")
        expect(results).to_be_visible()

        # Click the new workout button
        page.click("#new-workout-btn")

        # Results should be hidden again
        expect(results).to_be_hidden()
