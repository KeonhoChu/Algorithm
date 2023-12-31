SELECT B.BOOK_ID, A.AUTHOR_NAME, TO_CHAR(B.PUBLISHED_DATE, 'YYYY-MM-DD') as PUBLISHED_DATE 
FROM BOOK B, AUTHOR A
WHERE B.AUTHOR_ID = A.AUTHOR_ID
AND B.CATEGORY = '경제'
ORDER BY B.PUBLISHED_DATE;