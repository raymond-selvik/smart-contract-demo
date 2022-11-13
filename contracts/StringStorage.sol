pragma solidity >=0.6.0 <0.9.0;

contract StringStorage 
{
 mapping(address => string) public addressToString;

    function store(string memory _string) public {
        addressToString[msg.sender] = _string;
    }

    function retrieve() public view returns(string memory) {
        require(bytes(addressToString[msg.sender]).length > 0, "No string for address");
        return addressToString[msg.sender];
    }

    function getSenderAddress() public view returns(address)
    {
        return(msg.sender);
    }

}