import express from 'express';
import { registrarUsuario,login, actulizarUsuario,devolverUsuario,devolverUsuarios} from '../src/controllers/usuario.controller.js';
import asyncHandler from "express-async-handler"
import { validarUsuario ,validadAdmin} from '../src/middlewares.js';

export const usuarioEnrutador = express.Router();

//captura el controlador asycrono
usuarioEnrutador.post("/registro",asyncHandler(registrarUsuario));
usuarioEnrutador.post("/login",asyncHandler(login));
usuarioEnrutador.put("/actualizar-usuario",asyncHandler(validarUsuario),asyncHandler(actulizarUsuario));
usuarioEnrutador.get("/usuario",asyncHandler(validarUsuario),asyncHandler(devolverUsuario));
usuarioEnrutador.get("/listausuario",asyncHandler(validarUsuario),asyncHandler(validadAdmin),asyncHandler(devolverUsuarios));