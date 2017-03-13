import unittest
from flask import Flask, jsonify
from flask import request
from flask import make_response
from flask import abort


app = Flask(__name__)

# TODO store data safer than in-memory
global votes 
global candidates   
global globalCounter

globalCounter = 0
votes = {}
candidates = {}


@app.route('/candidates', methods=['GET'])
def get_candidates():   
    result = []

    for id, votesCount in candidates.items():        
        result.append({
           "candidateId": id,
           "voteCount": votesCount,   
           "percents" : round(votesCount * 100 / globalCounter, 2)
        })        
    return jsonify(result)

@app.route('/vote', methods=['POST'])
def vote():
    global globalCounter

    maxVotes = 3

    if not request.json or not 'userKey' in request.json or not 'candidateId' in request.json:
        abort(400)    
    vote = {
        "userKey": request.json["userKey"],
        "candidateId": request.json["candidateId"]    
    }

    # TODO thread-safe access
    if vote['userKey'] not in votes: votes[vote['userKey']] = 0
    if votes[vote['userKey']] < maxVotes: 
        votes[vote['userKey']] += 1
        if vote['candidateId'] not in candidates: candidates[vote['candidateId']] = 0
        candidates[vote['candidateId']] += 1
        globalCounter += 1
    else:
        abort(403)

    return jsonify({'vote': vote}), 201

@app.route('/votes', methods=['GET'])
def get_votes(): 
    return jsonify(votes)

if __name__ == '__main__':        
    app.run()
