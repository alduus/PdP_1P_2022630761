;Castillo Reyes Diego
;Escamilla Reséndiz Aldo
;Lopez Sanchez Adair
;Yañez Martinez Marthon Leobardo

(defun fibonacci (n)
  (cond
    ((= n 0) '(0))
    ((= n 1) '(0 1))
    (t (let ((fib-sequence (list 0 1))
             (prev-prev 0)
             (prev 1)
             (current 0))
         (loop repeat (- n 1) do
           (setf current (+ prev-prev prev))
           (setf prev-prev prev)
           (setf prev current)
           (push current fib-sequence))
         (reverse fib-sequence)))))

(let ((sequence (fibonacci 5)))
  (rotatef (first sequence) (second sequence))
  (print sequence))