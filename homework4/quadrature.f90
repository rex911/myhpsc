module quadrature
  contains    
    REAL(kind=8) FUNCTION trapezoid(f, a, b, n)
      IMPLICIT NONE
      real(kind=8), external:: f
      real(kind=8), intent(in):: a, b
      integer, intent(in) :: n
      integer ::i 
      REAL(kind=8) :: h,x,fsum
      real(kind=8) :: fj(n)
      h = (b-a)/(n-1)
      trapezoid = 0.0
            
      do i =1,n
        x = (i-1)*h+a
        fj(i) = f(x)
        fsum = fsum + fj(i)
      enddo
      trapezoid = h*fsum - 0.5*h*(fj(1)+fj(n))
    end function trapezoid
    subroutine error_table(f,a,b,nvals,int_true)
      implicit none
      real(kind=8), external :: f
      real(kind=8), intent(in) :: a,b,int_true
      integer, dimension(:), intent(in) :: nvals
      real(kind=8) :: t1, t2, elapsed_time, error, last_error, ratio, int_est
      integer :: i, n, tclock1, tclock2, clock_rate

      print *, " n trapezoid error ratio cpu time elapsed time"
      last_error = 0.0
      do i=1, size(nvals)
        n = nvals(i)
        call system_clock(tclock1)
        call cpu_time(t1)
        int_est = trapezoid(f, a, b, n)
        call cpu_time(t2)
        call system_clock(tclock2, clock_rate)
        error = abs(int_true - int_est)
        ratio = last_error/error
        last_error = error
        elapsed_time = float(tclock2 - tclock1)/float(clock_rate)
        print 11, n, int_est, error, ratio, t2-t1, elapsed_time
        11 format(i8, es22.14, es13.3, es13.3,f12.8,f12.8)
      enddo
    end subroutine error_table
end module quadrature
