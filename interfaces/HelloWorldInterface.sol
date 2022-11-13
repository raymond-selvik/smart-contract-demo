pragma solidity >=0.6.0 <0.9.0;

interface HelloWorldInterface
{

    function sayHello() external pure returns(string memory);

    function getCallerAddress() external view returns(address);
  
}