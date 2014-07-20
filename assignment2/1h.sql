select sum(f1.count * f2.count)
from frequency f1
join frequency f2 on f1.term = f2.term
where f1.docid = "10080_txt_crude" and
	  f2.docid = "17035_txt_earn"
group by f1.docid, f2.docid;