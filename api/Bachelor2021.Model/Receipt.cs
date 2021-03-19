using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;

namespace Bachelor2021.Model {
    public class Receipt {
        [Key]
        public int ReceiptId { get; set; }
        [Required]
        public double Amount { get; set; }
        [Required]
        public String Type { get; set; }
        [Required]
        public String Company { get; set; }
        [Required]
        public String Date { get; set; }
        public Image Image { get; set; }
    }
}

