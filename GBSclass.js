//We will create a Gaussian Elimination With Backsubstitution Javascript Class

class GaussianElimination {
    #p_int = null;

    constructor(A, b){
        this.A = A;
        this.b = b
        this.size = b.length;
    }

    AM() {

        const dimA = [this.A.length, this.A[0].length];
        const dimb = [1, this.b.length];
        
        if (dimA[0] != dimb[1]){
            console.log("Dimensions Do Not Match!");
            process.exit();
        }

        for (let i = 0; i < this.size; i++){
            this.A[i].push(this.b[i]);
        }
        this.myarray = A;
        return this.myarray;
    }

    AM_rf() {

        for (let i = 0; i < this.size -1; i++){
            for (let p = i; p < this.size; p++){
                if (this.myarray[p][i] != 0){
                    this.#p_int = p;
                    break;
                }
            }

            if (this.#p_int == null){
                console.log("No Unique Solution Exists!");
                process.exit();
            }

            if (this.#p_int != i){
                let temp = this.myarray[this.#p_int];
                this.myarray[this.#p_int] = this.myarray[i];
                this.myarray[i] = temp;
            }

            for (let j = i+1; j < this.size; j++){
                let mij = this.myarray[j][i]/this.myarray[i][i];
                this.myarray[j] = this.#transform(this.myarray[j], this.myarray[i], mij);
            }

        }
        return this.myarray;
    }

    x_values(){

        if(this.myarray[this.size - 1][this.size - 1] == 0){
            console.log("No Unique Solution Exists!");
            process.exit();
        }

        let x = Array(this.size-1).fill(0)
        x[this.size - 1] = this.myarray[this.size-1][this.size]/this.myarray[this.size - 1][this.size - 1];
        for (let i = this.size-2; i > -1; i--){
            let sum = this.#sum_func(this.myarray, x, i)
            x[i] = (this.myarray[i][this.size] - sum)/this.myarray[i][i];
        }
        return x;
    }

    #transform(array1, array2, mult){
        let new_array = [];
        for (let k = 0; k < array1.length; k++){
            new_array.push(array1[k] - mult*array2[k])
        }
        return new_array;
    }

    #sum_func(array, x_vec, index){
        let sum = 0;
        for (let j = index + 1; j < this.size; j++){
            sum += array[index][j]*x_vec[j];
        }
        return sum
    }

}

//Example
const A = [[1.0,-1.0,2.0,-1.0],
            [2.0,-2.0,3.0,-3.0],
            [1.0,1.0,1.0,0.0],
            [1.0,-1.0,4.0,3.0]];

const b = [-8,-20,-2,4,1];

const gauss = new GaussianElimination(A, b);
console.log(gauss.AM());
console.log(gauss.AM_rf());
console.log(gauss.x_values());
