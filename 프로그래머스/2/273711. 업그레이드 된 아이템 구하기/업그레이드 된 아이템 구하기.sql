-- 코드를 작성해주세요
WITH Q AS
(SELECT B.ITEM_ID FROM ITEM_INFO AS A INNER JOIN ITEM_TREE AS B ON A.ITEM_ID=B.PARENT_ITEM_ID
WHERE A.RARITY='RARE' AND B.PARENT_ITEM_ID IS NOT NULL)

SELECT Q.ITEM_ID, ITEM_NAME, RARITY FROM Q INNER JOIN ITEM_INFO AS B ON Q.ITEM_ID=B.ITEM_ID
ORDER BY Q.ITEM_ID DESC
