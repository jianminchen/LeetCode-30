# Write your MySQL query statement below
delete P2
from Person P1, Person P2
where P1.Email = P2.Email and P1.Id < P2.Id 
