using Bachelor2021.Model;
using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Design;
using System;

namespace Bachelor2021.DataAccess {
    public class DataContext : DbContext {

        public DbSet<Receipt> Receipts { get; set; }
        public DataContext(DbContextOptions<DataContext> options) : base(options) { }

        class DataContextFactory : IDesignTimeDbContextFactory<DataContext> {
            public DataContext CreateDbContext(string[] args) {
                var connection = @"Server=(localdb)\MSSQLLocalDB;Database=Bachelor2021;Trusted_Connection=True;ConnectRetryCount=0";

                var optionsBuilder = new DbContextOptionsBuilder<DataContext>();
                optionsBuilder.UseSqlServer(connection, x => x.MigrationsAssembly("Bachelor2021.DataAccess.Maintenance"));

                return new DataContext(optionsBuilder.Options);
            }
        }
    }
}
