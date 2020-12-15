Feature: Test that pages have correct content
  Scenario: Blog page has correct title
    Given I am on the blog page
    Then There is a title on the page
    And the title tag has content "This is the blog page"
