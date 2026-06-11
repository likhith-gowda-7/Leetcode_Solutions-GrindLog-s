CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      select distinct emp_sal from (
        select id as emp_id,salary as emp_sal,dense_rank() over (order by salary desc) as emp_rank from Employee
      )as Ranking where emp_rank = N
  );
END