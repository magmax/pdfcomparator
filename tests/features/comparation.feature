
Feature:
  In order to compare PDFs
  I want to compare them by appearance

  Scenario: Without params, it must complain
    When I run exactly pdfcompare parameter
    Then the status is 1
    And the output contains "Format"

  Scenario: One file is equal to itself
    Given two PDFs, example1a.pdf and example1a.pdf
    When I run pdfcompare over them
    Then the status is 0

  Scenario: One file is not equal to a different one
    Given two PDFs, example1a.pdf and example2a.pdf
    When I run pdfcompare over them
    Then the status is 2
    And the output contains "Different number of pages (1 vs 4)"

  Scenario Outline: Similar files are identified
    Given two PDFs, <pattern> and <current>
    When I run pdfcompare over them
    Then the status is 0

  Examples:
    | pattern       | current       |
    | example1a.pdf | example1a.pdf |
    | example2a.pdf | example2b.pdf |
    | example3a.pdf | example3b.pdf |

  Scenario Outline: Different documents
    Given two PDFs, <pattern> and <current>
    When I run pdfcompare over them
    Then the status is 2
    And the output contains "<output>"

  Examples:
    | pattern       | current       | output    |
    | example1a.pdf | example2a.pdf | Different number of pages (1 vs 4) |
    | example1a.pdf | example3a.pdf | Page 1 is different |

  Scenario Outline: Differences are conmutative
    Given two PDFs, <pattern> and <current>
    When I run pdfcompare over them
    Then the status is 2
    And the output contains "<output>"

  Examples:
    | pattern       | current       | output    |
    | example1a.pdf | example3a.pdf | Page 1 is different |
    | example3a.pdf | example1a.pdf | Page 1 is different |


  Scenario: First file does not exist
    Given two PDFs, inexistent and example1a.pdf
    When I run pdfcompare over them
    Then the status is 2
    And the output contains "Couldn't open file"
