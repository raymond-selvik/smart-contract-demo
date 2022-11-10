pragma solidity >=0.6.0 <0.9.0;

contract StringStorage 
{
 mapping(address => string) public addressToString;

    function store(string memory _string) public {
        addressToString[msg.sender] = _string;
    }

    function retrieve() public view returns(string memory) {
        return addressToString[msg.sender];
    }

}