Feature: Tests for Instagram application

Scenario: Successful Login
    Given I open login page
    When I login with email and password
    Then I am on main page