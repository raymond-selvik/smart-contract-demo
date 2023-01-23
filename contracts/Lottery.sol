pragma solidity ^0.8.7;

contract Lottery 
{
    address public owner;
    address[] public players;

    constructor() {
        owner = msg.sender;
    }

    function enterLottery() payable public {
        require(msg.sender != owner);
        require(msg.value == 100e18);

        players.push(msg.sender);
    }

    function pickWinner() public{
         
        require(msg.sender == owner);
        uint256 index = random() % players.length;

        address payable  winner = payable(players[index]);
        winner.transfer(address(this).balance);
        players = new address[](0);
    }

    
    function random() private view returns(uint){
         return uint(keccak256(abi.encodePacked(block.difficulty, block.timestamp, players)));
    }
}