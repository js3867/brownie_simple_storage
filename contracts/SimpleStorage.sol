// SPDX-License-Identifier: MIT

pragma solidity >=0.6.0 <0.9.0;

contract SimpleStorage {
    // uint256 public favoriteNumber = 420;
    // can remove public and instead use dedicated VIEW retrieve() function
    uint256 favoriteNumber = 420; // <-- SimpleStorage[0] (Solidity storage)
    bool favoriteBool = true; // <-- SimpleStorage[1]

    // like creating a new Type
    struct People {
        uint256 favoriteNumber;
        string name;
        // uint256[] numbers;
    }

    // basically a constructor
    // People public person = People({favoriteNumber: 2,name: "Jimmy"});
    // Array -- a list of objects
    People[] public people; // <-- ArrayName[] w/ empty sq.brackets is dynamic in size
    mapping(string => uint256) public nameToFavoriteNumber;

    function addPerson(string memory _name, uint256 _favoriteNumber) public {
        people.push(People({favoriteNumber: _favoriteNumber, name: _name}));
        nameToFavoriteNumber[_name] = _favoriteNumber;
    }

    // function store(uint256 _favoriteNumber) public {
    //     favoriteNumber = _favoriteNumber;
    // }
    // update version to work with new deploy.py (Lesson 4)
    function store(uint256 _favoriteNumber) public returns (uint256) {
        favoriteNumber = _favoriteNumber;
        return favoriteNumber;
    }

    // view, pure
    function retrieve() public view returns (uint256) {
        return favoriteNumber;
    }

    // // view, pure
    // function retrieveNumbers() public view returns(uint256[]) {
    //     return numbers;
    // }

    // -- NOTES --
    //
    // what are the numbers after some of these Types?
    // -- uint == unsigned integer, ONLY positive integers
    // -- ..256 == not 100% why but is considered best practice for smart conts
    //             see here: https://docs.soliditylang.org/en/v0.4.21/types.html#value-types
    //
    // uint256 favoriteNumber will initialize as NULL by default if not initialized otherwise
    // uint256 will be 'internal' (/private) if not declared 'public' and will not be viewable
    //
    // 'view' and 'pure' keywords do not require a txn
    // the are 'non-state changing functions
    //
    // 'memory' vs 'storage' -> function addPerson(string memory _name, ..
    //  memory will save info only during execution of the function/contract call
    //  storage will persist even after function executes
    //  - string is technically an array of chars, so needs to be assigned one of these options
    //
}
