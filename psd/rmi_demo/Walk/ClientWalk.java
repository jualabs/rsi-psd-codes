import java.rmi.Naming;
import java.rmi.RemoteException;
import java.util.Scanner;

public class ClientWalk {
	
	public static void main(String[] args) {
		
		IWalk rwalk = null;
		Scanner input = new Scanner(System.in);
		
		try {
			String objname =  "rmi://localhost/walkserver";
			System.out.println("Procurando pelo objeto " + objname);
			rwalk = (IWalk) Naming.lookup(objname);
		}
		catch (Exception e) {
			System.err.println("Problemas ao executar o lookup! " + e);
			e.printStackTrace();
			System.exit(2);
		}
		while(true) {
			try {
			
				System.out.print("Digite o número de passos que deseja movimentar ou 't' para total de passos já realizados ou 's' para sair: ");
				String inputString = input.next();
				if(inputString.equals("t")) {
			    		System.out.println("\n" + rwalk.total());
				}
				else if(inputString.equals("s")) {
			    		System.exit(0);
				}
				else {
					int steps = Integer.parseInt(inputString);
					rwalk.move(steps);
				}
			}
			catch (RemoteException re) {
				System.err.println("Problemas durante chamada remota! " + re);
				re.printStackTrace();
				System.exit(3);
			}
			catch (NumberFormatException nfe) {
				System.out.println("Digite um valor válido!");
				continue;	
			}
		}
	}
}
