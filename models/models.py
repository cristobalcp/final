# -*- coding: utf-8 -*-

from odoo import models, fields, api

# Modelo Libro   
class Libro(models.Model):
    _name = 'final.libro'
    _description = "Final Libro"

    name = fields.Char(string="Titulo", required=True)
    datetime = fields.Datetime(string='Dia Lanzamiento', required=True)    
    pages = fields.Integer(string='Paginas')    
    price = fields.Float(string="Precio (€)")
    sinopsis = fields.Char(string="Sinopsis")
    isbn = fields.Char(string="Isbn")

    # Lo relacionamos con el modelo Autor
    autor_id = fields.Many2one('final.autor',
        ondelete='cascade', string="Autor", required=True, default=lambda self: self.env.user)
    
    # Lo relacionamos con el modelo Editorial
    editorial_id = fields.Many2one('final.editorial',
        string="Editorial", required=True, default=lambda self: self.env.user)

# Modelo Autor   
class Autor(models.Model):
    _name = 'final.autor'
    _description = "Final Autor"

    name = fields.Char(string="Nombre", required=True)
    nationality = fields.Char(string="Nacionalidad")
    year = fields.Integer(string="Año")
    sex = fields.Char(string="Sexo")

    # Lo relacionamos con el modelo Libro
    libro_id = fields.One2many('final.libro',
        'autor_id', string="Libros", default=lambda self: self.env.user)

# Modelo Editorial   
class Editorial(models.Model):
    _name = 'final.editorial'
    _description = "Final Editorial"

    name = fields.Char(string="Nombre", required=True)
    address = fields.Char(string="Direccion")
    email = fields.Char(string="Email")
    phone = fields.Char(string="Telefono")

    # Lo relacionamos con el modelo Libro
    # libro_id = fields.One2many('final.libro',
    #     'editorial_id', string="Libros", default=lambda self: self.env.user)


