pragma solidity >=0.6.0 <0.9.0;

contract HelloWorld 
{

    function sayHello() public pure returns(string memory)
    {
        return("Hello World!");
    }

       function getCallerAddress() public view returns(address)
    {
        return(msg.sender);
    }
}