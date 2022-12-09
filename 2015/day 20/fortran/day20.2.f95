program day20
   implicit none

   integer :: num, end, arr_sum
   integer, allocatable :: prime_lst(:)
   integer, allocatable :: factor_arr(:)
   integer, allocatable :: divisor_arr(:)

   ! main

   Open (10, file='..//input.txt')
   Read (10, *) end

   prime_lst = sieve_of_eratosthenes(end)

   do num = 1, end
      factor_arr = prime_factor(num, prime_lst)
      divisor_arr = divisors(factor_arr)
      arr_sum = conditional_sum(divisor_arr, num, 11)
      if (arr_sum > end) exit

      if (mod(num, 10000) == 0) print *, num, sum(divisor_arr), end
   end do
   print *, num

contains
   function get_unique_array(input_array) result(unique_array)
      implicit none
      !-----------------------------------------------------------------------------
      ! Description:
      !   Find the unique numbers in a SORTED! array
      !
      ! Method:
      !   Count the amount of times a number occurs in the list.
      !   Use an index to skip that amount to go to the next number
      !
      ! Code Description:
      !   Language: Fortran 90.
      !   This code is written to JULES coding standards v1.
      !   http://jules-lsm.github.io/coding_standards/standard_code_templates/index.html
      !-----------------------------------------------------------------------------

      ! variables
      integer, intent(in) :: input_array(:)
      integer, allocatable :: unique_array(:)
      integer index, index_value

      ! main
      allocate (unique_array(0))
      index = 1
      do while (index <= SIZE(input_array))
         index_value = input_array(index)
         unique_array = [unique_array, index_value]
         index = index + count(input_array == index_value)
      end do

   end function get_unique_array

   function sieve_of_eratosthenes(N) result(prime_array)
      implicit none

      !-----------------------------------------------------------------------------
      ! Description:
      !   Finds primes until N
      !
      ! Method:
      !   This code makes use of the sieve of Atkin.
      !   The pseudocode from wikipedia.org is used as reference.
      !   https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
      !
      !   This is partially optimised myself
      !
      ! Code Description:
      !   Language: Fortran 90.
      !   This code is written to JULES coding standards v1.
      !   http://jules-lsm.github.io/coding_standards/standard_code_templates/index.html
      !-----------------------------------------------------------------------------

      ! Subroutine arguments
      integer, intent(in) :: N         ! limit

      ! Local variables
      integer, dimension(N) :: is_prime
      integer :: number                ! number which is currently being checked
      integer :: prime_amount          ! amount of primes found
      integer :: prime_array_index     ! value to remember the index
      integer, allocatable :: prime_array(:)

      !-----------------------------------------------------------------------------

      is_prime = 1

      do number = 2, nint(sqrt(real(N)))
         if (is_prime(number) == 1) then

            is_prime(number*number:N:number) = 0
         end if
      end do

      ! Now we have a logical list of primes, make a new list of amount of TRUE called prime_array
      prime_amount = sum(is_prime) - 1
      allocate (prime_array(prime_amount))

      prime_array_index = 1
      ! For every value in prime_array; if index is 1; add index to prime_array
      do number = 2, N
         if (is_prime(number) == 1) then
            prime_array(prime_array_index) = number
            prime_array_index = prime_array_index + 1
         end if
      end do
   end function sieve_of_eratosthenes

   function prime_factor(n, prime_array) result(prime_factor_array)
      implicit none
      !-----------------------------------------------------------------------------
      ! Description:
      !   Find the prime factors from a number
      !
      ! Method:
      !   Prime factors are the multiplied combination of prime numbers that a number exists of
      !   We use a list of prime numbers to iterate to the next prime factor.
      !   Divide by prime factor until not possible anymore, while lowering N by it.
      !   Repeat until divide is not whole number, then go to next prime.
      !
      ! Code Description:
      !   Language: Fortran 90.
      !   This code is written to JULES coding standards v1.
      !   http://jules-lsm.github.io/coding_standards/standard_code_templates/index.html
      !-----------------------------------------------------------------------------

      ! variables
      integer, intent(in) :: n
      integer, intent(inout) :: prime_array(:)
      integer, allocatable  :: prime_factor_array(:)
      integer :: prime_index, factor, new_n

      ! maiin
      factor = 2
      prime_index = 1
      new_n = n
      allocate (prime_factor_array(0))

      ! while factor is bigger or equal then N
      do while (factor <= (new_n))
         if (mod(new_n, factor) == 0) then
            ! append
            prime_factor_array = [prime_factor_array, factor]

            ! lower N
            new_n = new_n/factor
         else
            ! go to next prime factor
            prime_index = prime_index + 1
            factor = prime_array(prime_index)
         end if
      end do

   end function prime_factor

   recursive function rec_gen(factors, n, omega, ps) result(mult_lst)
      implicit none
      !-----------------------------------------------------------------------------
      ! Description:
      !   Prime factors into divisors using recursion.
      !
      ! Method:
      !   Uses recursion to make a list of all divisors.
      !   The original method used a generator, however I used an array for simplicity.
      !   Tim Peters method was used from stackoverflow for this.
      !   TODO: Requires more experimentation to fully understand
      !   https://stackoverflow.com/questions/1010381/python-factorization
      !
      ! Code Description:
      !   Language: Fortran 90.
      !   This code is written to JULES coding standards v1.
      !   http://jules-lsm.github.io/coding_standards/standard_code_templates/index.html
      !-----------------------------------------------------------------------------

      ! variables
      integer, intent(in) :: n, omega
      integer, intent(in) :: factors(:), ps(:)
      integer, allocatable :: mult_lst(:), pows(:), q_lst(:)
      integer :: j, q

      ! main
      allocate (mult_lst(0))

      ! return list of just 1
      if (n == omega) then
         mult_lst = [mult_lst, 1]
         return
      end if

      allocate (pows(1))
      pows = 1

      do j = 1, count(factors == ps(n))
         pows = [pows, pows(j)*ps(n)]
      end do

      ! recursion
      q_lst = rec_gen(factors=factors, ps=ps, omega=omega, n=(n + 1))

      do q = 1, size(q_lst)
         mult_lst = [mult_lst, q_lst(q)*pows]
      end do
   end function rec_gen

   function divisors(factors_array) result(divisors_array)
      implicit none
      !-----------------------------------------------------------------------------
      ! Description:
      !   Prime factors into divisors using recursion.
      !
      ! Method:
      !   Uses recursion to make a list of all divisors.
      !   The original method used a generator, however I used an array for simplicity.
      !   Tim Peters method was used from stackoverflow for this.
      !   TODO: Requires more experimentation to fully understand
      !   https://stackoverflow.com/questions/1010381/python-factorization
      !
      ! Code Description:
      !   Language: Fortran 90.
      !   This code is written to JULES coding standards v1.
      !   http://jules-lsm.github.io/coding_standards/standard_code_templates/index.html
      !-----------------------------------------------------------------------------

      ! variables
      integer, allocatable, intent(in) :: factors_array(:)
      integer, allocatable :: divisors_array(:)
      integer, allocatable :: ps(:)       ! all unique values of array
      integer              :: omega

      ! main
      ps = get_unique_array(factors_array)
      omega = size(ps) + 1

      divisors_array = rec_gen(faAlso
      cond_sum = 0
      do index = 1, size(divisors_array)
         if ((divisors_array(index)*50) >= max_num) then
            cond_sum = cond_sum + divisors_array(index)*mult
         end if
      end do

   end function conditional_sum
end program day20
