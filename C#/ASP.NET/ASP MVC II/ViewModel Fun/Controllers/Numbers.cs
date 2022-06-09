using Microsoft.AspNetCore.Mvc;
using ViewModel_Fun.Models;
namespace ViewModel_Fun.Controllers;
    public class NumbersController : Controller
    {
        [HttpGet("/numbers")]
        public IActionResult numbers()
        {
            int[] number = new int[] {
                1,
                2,
                3,
                10,
                43,
                5
        };
            return View("numbers", number);
        }
    }