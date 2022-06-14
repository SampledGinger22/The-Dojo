﻿using System.Diagnostics;
using Microsoft.AspNetCore.Mvc;
using Login_and_Registration.Models;

namespace Login_and_Registration.Controllers;

public class HomeController : Controller
{

    private MyContext _context;

    public HomeController(MyContext context)
    {
        _context = context;
    }

    public IActionResult Index()
    {
        return View();
    }

    [ResponseCache(Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)]
    public IActionResult Error()
    {
        return View(new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
    }
}
