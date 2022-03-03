from brownie import SimpleStorage, accounts


def test_deploy():
    # 1. Arrange -- set stuff up for testing
    account = accounts[0]

    # 2. Act -- deploy SimpleStorage smart contract
    simple_storage = SimpleStorage.deploy({"from": account})
    starting_value = simple_storage.retrieve()
    expected = 420  # <<< SimpleStorage favouriteNumber

    # 3. Assert -- compare that starting value is what we expect
    assert starting_value == expected

    # test using:
    # $ brownie test


def test_udpating_storage():
    # Arrange
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})

    # Act
    expected = 15
    simple_storage.store(expected, {"from": account})

    # Assert
    assert expected == simple_storage.retrieve()


# to only run certain test:
# brownie test -k test_updating_storage

# opens python's post-mortem style tool which allows the values
# of differnt objects of the script to be printed to display
# their value for interrogation
# brownie test -pdb

# slightly more robust and insightful testing:
# brownie test -s

# see docs.pytest.org
