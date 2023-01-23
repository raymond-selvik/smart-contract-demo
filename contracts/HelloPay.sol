pragma solidity >=0.6.0 <0.9.0;

contract HelloPay
{

    function getBalance() public view returns(uint256)
    {
        return(address(this).balance);
    }

    function pay() public payable returns(string memory)
    {
        return("Thank you for paying");
    }
}