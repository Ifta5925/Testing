Feature: Test navigation between apps
  We can have longer description
  That can span a few lines

  Scenario: Homepage can go to Blog
    Given I am on the homepage
    When I click on the "Go to blog" link
    Then I am on the blog page

  Scenario: Blog page can go to homepage
    Given I am on the blog page
    When I click on the "Go to home" link
    Then I am on the homepage