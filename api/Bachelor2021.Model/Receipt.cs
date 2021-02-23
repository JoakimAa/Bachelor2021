using System;
using System.ComponentModel.DataAnnotations;

namespace Bachelor2021.Model {
    public class Receipt {
        public int ReceiptId { get; set; }
        [Required]
        public double Amount { get; set; }
        [Required]
        public String Type { get; set; }
        [Required]
        public String Company { get; set; }
        [Required]
        public String Date { get; set; }
    }
}

