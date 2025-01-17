import express from 'express';
import { registrarUsuario } from '../src/controllers/usuario.controller.js';
import asyncHandler from "express-async-handler"

export const usuarioEnrutador = express.Router();

//captura el controlador asycrono
usuarioEnrutador.post("/registro",asyncHandler(registrarUsuario));
