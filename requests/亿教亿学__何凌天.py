import requests
import json

def parse_one_page(s, query,nextid):
    """
    Parse all the questions on one page and return the first and last id for question to generate new query string
    Args:
        s: current session
        query: str, query str
        nextid: the number id of the first question that is going to be processed
    Returns:
        firstid: the first id on the page
        lastid: the last id on the page
        nextid: the number id of question that will be denotated next. e.g. 6 questions have been processed in the first page, then nextid is 7, whhich is the number id for first question processed in the next page
    """
    result = s.get('http://10.0.0.51/api/teacher/yj_questions/choice', headers=s.headers, params=query)
    # check if it's the last page
    ret = json.loads(result.text)
    qid_list = []
    if len(ret['retlist'])!=0:
        for i, ret_result in enumerate(ret['retlist']):
            qid_list.append(str(ret_result[0]))
            question = ret_result[2]
            with open('/Users/lyndon/Documents/白月黑羽python/yjyx/{}.html'.format(int(nextid)+i), 'w') as f:
                f.write(question)
        firstid = qid_list[0]
        lastid = qid_list[-1]
        nextid += len(qid_list)
    else:
        print("No more pages, process finished")
        firstid,lastid,nextid = None,None,None
    return firstid, lastid, nextid


def main():
    # login
    s = requests.Session()
    response = s.post('http://10.0.0.51/api/teacher/loginreq', data = {
    'username':'jcyrss',
    'password':'sdfsdf5%'
    })
    # initiate a query string
    query  = {
    'action': 'list',
    'subjectid':'1',
    'firstid':'0',
    'lastid':'0',
    'direction':'NEXT',
    'onlysearchmine':'false',
    'tags': '{"level":"","customtags":[]}',
    'sgttags': '{"textbookid":1,"textbookunitid":"ZJ_1_2_2","subjectid":["1"],"textbookverid":["1"],"gradeid":["1"],"textbookvolid":["1"]}'}
    nextid = 1

    while query['firstid']!=None:
        firstid, lastid, nextid= parse_one_page(s,query,nextid)
        print(firstid, lastid, nextid)
        query.update({'firstid':firstid, 'lastid':lastid})

if __name__ == '__main__':
    main()
