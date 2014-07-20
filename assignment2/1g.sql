select sum(a.value * b.value) val
from a 
join b on b.row_num = a.col_num
where a.row_num = 2 and b.col_num = 3
group by a.row_num, b.col_num;
