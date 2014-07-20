create temp view frequency_ex as
SELECT * FROM frequency
UNION
SELECT 'q' as docid, 'washington' as term, 1 as count 
UNION
SELECT 'q' as docid, 'taxes' as term, 1 as count
UNION 
SELECT 'q' as docid, 'treasury' as term, 1 as count;

select distinct sum(f1.count * f2.count) s
from frequency_ex f1
join frequency_ex f2 on f1.term = f2.term
where f1.docid = "q" and
	  f2.docid <> "q"
group by f1.docid, f2.docid
order by s desc
limit 1;