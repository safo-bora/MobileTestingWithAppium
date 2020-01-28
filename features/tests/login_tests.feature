Feature: Tests for Instagram application

Scenario: Successful Login
    Given I open login page
    When I login with romanchuk.kateryna@gmail.com and Work2019
    Then I am on main page