package com.talktrack.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.servlet.mvc.support.RedirectAttributes;

@Controller
public class PageController {

    @GetMapping({"/", "/index"})
    public String index() {
        return "index"; // templates/index.html
    }

    @GetMapping("/crear")
    public String crear() { return "crear"; }

    @PostMapping("/crear")
    public String handleCrear(@RequestParam(required=false) String nombre,
                              @RequestParam(required=false) String apellido,
                              RedirectAttributes redirectAttrs) {
        // Aquí podrías guardar el usuario en la base de datos.
        redirectAttrs.addFlashAttribute("mensaje", "Cuenta creada para: " + (nombre!=null?nombre:""));
        return "redirect:/";
    }

    @GetMapping("/olvide")
    public String olvide() { return "olvide"; }
}
