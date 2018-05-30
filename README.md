# The Q-CTRL Back-end Challenge

The goal of this challenge is to create a web-based API using [Django](https://www.djangoproject.com/). The API should be backed by a [MySQL](https://www.mysql.com/) database and conform to the [JSON API](http://jsonapi.org/) specification.

To get started please fork this repository and when you're finished create a pull request.

## Brief

The brief has been divided into 6 features:

1.  [Create a pulse](#create-pulse)
1.  [List all pulses](#list-pulses)
1.  [Retrieve a pulse](#retrieve-pulse)
1.  [Modify a pulse](#modify-pulse)
1.  [Delete a pulse](#destroy-pulse)
1.  [Upload a pulse](#upload-pulse)

---

### Create pulse

Implement an endpoint that creates a pulse. A pulse has a name (string),
maximum rabi rate(float, between 0 and 100) and polar angle(float, between 0 and 1).

##### Scenario 1: Create pulse

    When I request POST `/pulses/` with
        a name of "primitive",
        a maxumum rabi rate of 1
        and a polar angle of 0.5
    Then I should see the new pulse.

##### Scenario 2: Pulse validation

    When I request POST `/pulses/` with an empty body
    Then I should see a 400 bad request response
    And I should see error messages.

---

### List pulses

Implement an endpoint that lists evaluations.

#### Scenarios

##### Scenario 1: Show pulses

    Given I have 10 pulses
    When I request GET `/pulses/`
    Then I should see a list of 5 evaluations with ids from 1 to 5.

##### Scenario 2: Show more pulses

    Given I have 10 pulses
    When I request GET `/pulses/?page=2`
    Then I should see 5 evaluations with the ids from 5 to 10.

---

### Retrieve pulse

Implement an endpoint that can retrieve a specific pulse.

#### Scenarios

##### Scenario 1: Show pulse

    Given I have a pulse with the id of 1
    When I request GET `/pulses/1`
    Then I should see pulse 1.

---

### Modify pulse

Implement an endpoint that can retrieve a specific pulse.

#### Scenarios

##### Scenario 1: Modify pulse name

    Given I have a pulse with the id of 1
    And is named 'wimperis 1'
    When I send a PATCH `/pulses/1` request with a new name `primitive` in the body
    Then I should see pulse 1 named `primitive``.

---

### Destroy pulse

Implement an endpoint that can destroy a specific pulse.

#### Scenarios

##### Scenario 1: Modify pulse name

    Given I have a pulse with the id of 1
    When I send a DELETE `/pulses/1` request
    Then I should see a `no content` response.

---

### Upload pulse

Implement an endpoint that can accept a CSV file where each row represents a pulse.
