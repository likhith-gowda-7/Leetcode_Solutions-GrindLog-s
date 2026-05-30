SELECT e.name
FROM Employee e
JOIN Employee sub ON sub.managerId = e.id
group by e.id
having COUNT(*) > 4;
