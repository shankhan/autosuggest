from flask import request, jsonify
from flask_restful import Resource
from Model import Autocomplete
from Model import db

class Gene(Resource):
    def get(self):
        q = request.args.get('query', None)
        species = request.args.get('species', None)
        limit = request.args.get('limit', default=10, type=int)

        query = db.session.query(Autocomplete.display_label, Autocomplete.species)
        if q is not None:
            search = "{}%".format(q)
            query = query.filter(Autocomplete.display_label.like(search))

        if species is not None:
            search = "{}%".format(species)
            query = query.filter(Autocomplete.species.like(search))

        result = query.limit(limit).all()
        
        genes = list()
        for r in result:
            genes.append({ 'species': r.species, 'display_label': r.display_label })

        return jsonify(genes)